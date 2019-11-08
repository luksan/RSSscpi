from .. import znb
from ..scpi.class_property import SCPIProperty
from ..gen import ZNB_gen


class Diagram:
    def __init__(self, n, instrument):
        """
        :param n: Number of the diagram area
        :param instrument: Reference to the Instrument
        """
        self._instr = instrument
        self.n = n

    @property
    def instrument(self) -> "znb.ZNB":
        return self._instr

    def delete(self):
        # FIXME: make some kind of callback to update all remaining Diagram instances?? requires a weakref dict.
        """
        Remove the diagram area. Note that this will re-number all remaining diagrams, so use with care.
        Renumbering causes the diagram name to be reset to the diagram number, this is arguably a FW bug.
        Also deletes all traces assigned to the diagram.
        :return:
        """
        self.WINDow.STATe.w("OFF")

    def select_diagram(self):
        """
        Make the diagram the active diagram.

        :return: None
        """
        self.is_maximized = self.is_maximized

    @property
    def WINDow(self) -> ZNB_gen.DISPlay.WINDow:
        return self.instrument.scpi.DISPlay.WINDow[self.n]

    @property
    def LAYout(self) -> ZNB_gen.DISPlay.LAYout:
        return self.instrument.scpi.DISPlay.LAYout

    _WIN = ZNB_gen.DISPlay.WINDow

    state = SCPIProperty(_WIN.STATe, bool, parent_prop=WINDow)
    """
    Enable/disable the diagram.
    Note that disabling the diagram will renumber all the remaining diagrams on the instrument,
    and delete all traces that are assigned to the diagram.
    """

    is_maximized = SCPIProperty(_WIN.MAXimize, bool, parent_prop=WINDow)
    """
    Displays the diagram on top of the other diagrams, filling the whole screen.
    """

    name = SCPIProperty(_WIN.NAME, str, parent_prop=WINDow)
    """
    The diagram name, shown in upper right corner. Returned with DISPlay:CATalog?
    """

    title = SCPIProperty(_WIN.TITLe.DATA, str, parent_prop=WINDow)
    """
    The diagram title, shown on screen.
    """

    title_is_visible = SCPIProperty(_WIN.TITLe.STATe, bool, parent_prop=WINDow)
    """
    Determines whether the diagram title is shown or not.
    """

    def save_screenshot(self, filename):
        """
        Take a screenshot containing only this diagram.

        :param filename: The filname under which the screenshot will be saved on the instrument.
        :return: a File object representing the captured screenshot
        :rtype: File
        """
        return self.instrument.save_screenshot(filename=filename, diagram=self)

    def query_assigned_traces(self):
        """
        Get the traces assigned to the diagram

        :return: A generator returning Traces
        """
        trace_list = self.WINDow.TRACe.CATalog.q()
        for trace_number, name in trace_list.comma_list_pairs():
            ch_no = self.instrument.CONFigure.TRACe.CHANnel.NAME.ID.q(name)
            ch = self.instrument.get_channel(ch_no)
            yield ch.get_trace(name=name)
