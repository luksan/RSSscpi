$(function () {

    var $table = $('table.cmd-table').DataTable( {
        dom: "ltrip",
        paging: false,
        fixedHeader: {headerOffset: 0},
        initComplete: function () {

            this.api().columns(".vna-col").every( function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo( $(column.footer()).empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );


                    select.append( '<option value="Y">Y</option>' );
                    select.append( '<option value="N">N</option>' );
            } );
        }
    } );

    // Apply the search
    $table.columns(0).every( function () {
        var that = this;

        $( 'input', this.footer() ).on( 'keyup change', function () {
            if ( that.search() !== this.value ) {
                that
                    .search( this.value )
                    .draw();
            }
        } );
    } );

    // move the filters to the top of the table
    $('.cmd-table tfoot tr').appendTo('.cmd-table thead');

    });
