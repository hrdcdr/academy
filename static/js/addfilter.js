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
        var condition_text = $('select#condition option:selected').text();
        var filter_text = $('input[name="selected"]').val();
        $('#listfilters').fadeIn('slow').append('<li>' + '"' +field_text + '"' + ' ' + condition_text + ' ' + '"' + filter_text + '"' + '</li>');
	});
});