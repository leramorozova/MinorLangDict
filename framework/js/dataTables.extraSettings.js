  
  // Function for the details row 
    function format ( d ) {
      // `d` is the original data object for the row, 'add' is a json key
      return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
          '<tr>'+
              '<td>Additional forms:</td>'+
              '<td>'+d.add+'</td>'+
          '</tr>'+
      '</table>';
    }

  // Data loading from json
    $(document).ready(function() {
      var table = $('#main_table').DataTable( {
          "ajax": "data.json", // json with dictionary data
          "columns": [
              {
                "className":      'details-control',
                "orderable":      false,
                "data":           null,
                "defaultContent": '',
              },
              { "data": "id" },
              { "data": "transcription" },
              { "data": "pos" },
              { "data": "audio" },
              { "data": "translation" },
              { "data": "rustranslation" }
          ],
          "order": [[1, 'asc']],
      } );
    
  // Opening and closing details
    $('#main_table tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = table.row( tr );
 
        if ( row.child.isShown() ) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child( format(row.data()) ).show();
            tr.addClass('shown');
        }
    } );

  // Individual column searching
    $('#main_table thead tr').clone(false).appendTo( '#main_table thead' ); // clone the row
    // specifying some css to remove styles cloned from the first row
    $('#main_table thead tr:eq(1) th').css('background-image','none').css('cursor','default').css('font-weight','300').each( function (i) {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="Search" />' );
        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );
    } );