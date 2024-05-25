$(document).ready(function () {
    $('#signup-form #password').on('input', function () {
        var password = $(this).val();
        $.ajax({
            url: '/check_password_strength/',
            data: {
                'password': password
            },
            dataType: 'json',
            success: function (data) {
                var strengthText = data.strength;
                var strengthClass = '';
                switch (strengthText) {
                    case 'Very strong':
                        strengthClass = 'strength-very-strong';
                        break;
                    case 'Strong':
                        strengthClass = 'strength-strong';
                        break;
                    case 'Moderate':
                        strengthClass = 'strength-moderate';
                        break;
                    case 'Weak':
                        strengthClass = 'strength-weak';
                        break;
                    case 'Too short':
                        strengthClass = 'strength-too-short';
                        break;
                }

                var strengthElement = $('#signup-form #password-strength');
                strengthElement.text(strengthText);
                strengthElement.attr('class', 'password-strength ' + strengthClass);
            }
        });
    });
});

