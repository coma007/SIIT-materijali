$(document).ready(function() {
	$('#exportDB').on('click', exportDB);
});

const exportDB = async () => {
    let filename = $('#db-export-name').val();

	await fetch(`/admin/export?filename=${filename}`, {
			method: 'GET',
			credentials: 'include',
        })
		.then(async (response) => {
            isJson = response.headers.get('content-type')?.includes('application/json');

            if (isJson) {
                response = await response.json();
                $('#resp-msg').text(response.message);
                $('#resp-msg').show();
                return;
            }
            window.open(`/admin/export?filename=${filename}`, '_blank');
        })
		.catch((error) => console.log(error));
}