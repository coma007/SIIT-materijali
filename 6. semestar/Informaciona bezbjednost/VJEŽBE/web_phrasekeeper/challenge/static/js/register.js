$(document).ready(function() {
	$('#register-btn').on('click', register);
});

function toggleInputs(state) {
	$('#username').prop('disabled', state);
	$('#password').prop('disabled', state);
	$('#email').prop('disabled', state);
	$('#register-btn').prop('disabled', state);
}

async function register() {

	toggleInputs(true);

	let card = $('#resp-msg');
	card.hide();

	let user = $('#username').val();
	let pass = $('#password').val();
	let email = $('#email').val();

	if ($.trim(user) === '' || $.trim(pass) === '' || $.trim(email) === '') {
		toggleInputs(false);
		card.text('Please fill out all the required fields!');
		card.attr('class', 'alert alert-danger');
		card.show();
		return;
	}

	await fetch('/graphql', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
                query: 'mutation($email: String!, $username: String!, $password: String!) { RegisterUser(email: $email, username: $username, password: $password) { message } }',
                variables: {
                    'email': email,
                    'username': user,
                    'password': pass,
                }
            }),
		})
		.then((response) => response.json())
        .then((response) => {
            if (response.data.RegisterUser) {
                card.text(response.data.RegisterUser.message);
                card.attr('class', 'alert alert-success');
                card.show();
                window.setTimeout(function() {
                    window.location.href = '/';
                }, 600);
                return;
            }
            else if (response.hasOwnProperty('errors')) {
                card.text(response.errors[0].message);
            }
            else {
                card.text('Something went wrong!');
            }
            card.attr('class', 'alert alert-danger');
            card.show();
        })
		.catch((error) => {
			card.text(error);
			card.attr('class', 'alert alert-danger');
			card.show();
		});

	toggleInputs(false);
}
