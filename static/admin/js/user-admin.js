(function($) {
    var $ = jQuery
    $(window).on('load',function() {
      var restaurantSelect = $('#id_restaurant');
      var locationSelect = $('#id_location');
      var adminCheckbox = $('#id_is_restaurant_administrator');
      var manCheckbox = $('#id_is_hiring_manager');
  
      // Hide the location select when the page is loaded
      restaurantSelect.prop("disabled", true);
      locationSelect.prop("disabled", true);
  
      // Show the location select if the checkbox is checked
      adminCheckbox.change(function() {
        if ($(this).prop('checked')) {
            restaurantSelect.prop("disabled", false);
        } else {
            restaurantSelect.prop("disabled", true);
            restaurantSelect.prop('selectedIndex', 0);
        }
      });
      manCheckbox.change(function() {
        if ($(this).prop('checked')) {
            locationSelect.prop("disabled", false);
        } else {
            locationSelect.prop("disabled", true);
            locationSelect.prop('selectedIndex', 0);
        }
      });
    });
  })(django.jQuery);