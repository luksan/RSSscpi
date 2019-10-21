from ..SCPI_property import SCPIProperty
from ..gen import ZNB_gen


class Diagram(ZNB_gen.DISPlay.WINDow):
    def __init__(self, n, instrument):
        """
        :param n: Number of the diagram area
        :param instrument: Reference to the Instrument
        :type instrument: ZNB
        """
        super(Diagram, self).__init__(parent=instrument.DISPlay)
        self.instrument = instrument
        self.n = n

    def delete(self):
        # FIXME: make some kind of callback to update all remaining Diagram instances?? requires a weakref dict.
        """
        Remove the diagram area. Note that this will re-number all remaining diagrams, so use with care.
        Renumbering causes the diagram name to be reset to the diagram number, this is arguably a FW bug.
        Also deletes all traces assigned to the diagram.
        :return:
        """
        self.STATe.w("OFF")

    def select_diagram(self):
        """
        Make the diagram the active diagram.

        :return: None
        """
        self.is_maximized = self.is_maximized

    _WIN = ZNB_gen.DISPlay.WINDow

    state = SCPIProperty(_WIN.STATe, bool)
    """
    Enable/disable the diagram.
    Note that disabling the diagram will renumber all the remaining diagrams on the instrument,
    and delete all traces that are assigned to the diagram.
    """

    is_maximized = SCPIProperty(_WIN.MAXimize, bool)
    """
    Displays the diagram on top of the other diagrams, filling the whole screen.
    """

    name = SCPIProperty(_WIN.NAME, str)
    """
    The diagram name, shown in upper right corner. Returned with DISPlay:CATalog?
    """

    title = SCPIProperty(_WIN.TITLe.DATA, str)
    """
    The diagram title, shown on screen.
    """

    title_is_visible = SCPIProperty(_WIN.TITLe.STATe, bool)
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
        trace_list = self.TRACe.CATalog.q()
        for trace_number, name in trace_list.comma_list_pairs():
            ch_no = self.instrument.CONFigure.TRACe.CHANnel.NAME.ID.q(name)
            ch = self.instrument.get_channel(ch_no)
            yield ch.get_trace(name=name)
