django.jQuery(document).ready(function() {
  django.jQuery( "table .add-another" ).each(function( index ) {
    django.jQuery(this).hide();
  });
  django.jQuery("table select").each(function(index, el) {
    tb = document.createElement('input');
    var input = django.jQuery(this);
    tb.type = 'text';
    tb.value = (this).options[(this).selectedIndex].text;
    (this).parentNode.insertBefore(tb, this);
    (this).style.display = 'none';
    tb.className = 'form-control vTextField';
  });
  django.jQuery( "table .vTextField" ).each(function( index ) {
    django.jQuery(this).css({'border-color': 'transparent', 'background': 'inherit', 'box-shadow': 'none'});
    // django.jQuery(this).prop("readonly", true);
    django.jQuery(this).prop("disabled", true);
  });
});

