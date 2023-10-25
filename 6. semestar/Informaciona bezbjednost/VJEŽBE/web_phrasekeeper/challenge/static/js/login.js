$(document).ready(function() {
	$('#login-btn').on('click', login);
});

const toggleInputs = (state) => {
	$('#username').prop('disabled', state);
	$('#password').prop('disabled', state);
	$('#login-btn').prop('disabled', state);
}


const login = async () => {

	toggleInputs(true);

	let card = $('#resp-msg');
	card.hide();

	let user = $('#username').val();
	let pass = $('#password').val();

	if ($.trim(user) === '' || $.trim(pass) === '') {
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
                query: 'mutation($username: String!, $password: String!) { LoginUser(username: $username, password: $password) { message, token } }',
                variables: {
                    'username': user,
                    'password': pass
                }
            }),
		})
		.then((response) => response.json())
        .then((response) => {
            if (response.data.LoginUser) {
                card.text(response.data.LoginUser.message);
                card.attr('class', 'alert alert-success');
                card.show();
                window.setTimeout(function() {
                    document.cookie = `session=${response.data.LoginUser.token}; SameSite=None; Secure`;
                    window.location.href = '/dashboard';
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
