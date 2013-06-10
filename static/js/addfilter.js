/**
 * Created with PyCharm.
 * User: user
 * Date: 04.06.13
 * Time: 0:55
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function(){
    $('#append').click(function() {
        var field_text = $('select#field option:selected').text()
        var field = $('select#field option:selected').val()
        var condition_text = $('select#condition option:selected').text();
        var condition = $('select#condition option:selected').val();
        var filter = $('input[name="selected"]').val();
        $('#listfilters').fadeIn('slow').append(
            '<li>' + '"' +field_text + '"' + ' ' + condition_text + ' ' + '"' + filter + '"' +
                '<input type="hidden" value="' + field + condition + '" name="condition">' +
                '<input type="hidden" value="' + filter + '" name="filter">'  + '</li>'
        );
	});
});