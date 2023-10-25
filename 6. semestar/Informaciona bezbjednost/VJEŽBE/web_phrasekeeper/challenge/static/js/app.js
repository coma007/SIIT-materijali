$(document).ready(function() {
	$('#addRecordBtn').on('click', addRecord);
	$('#cancelBtn').on('click', function() {
		$('#showFormBtn').click()
	});
	loadPasswords();
});

const loadPasswords = async () => {

	await fetch(`/graphql`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
                query: '{ getPhraseList { id, owner, type, address, username, password, note } }'
            }),
        })
		.then((response) => response.json())
		.then((response) => {
            if (response.data.getPhraseList && response.data.getPhraseList.length != 0) {
                populateTable(response.data.getPhraseList)
            }
        })
		.catch((error) => console.log(error));
}

const populateTable = (passList) => {

	$('#password-listing tbody').empty();
	$('#empty-table-msg').show();
	$('#password-listing').hide();

    for (entry in passList) {
        passInfo = passList[entry];

        rowData = `<tr id='${htmlEncode(passInfo.id)}_row'>`;

        if (passInfo.type == 'Email') {
            rowData += '<td>✉️ mail</td>';
        } else if (passInfo.type == 'App') {
            rowData += '<td>📱 app</td>';
        } else {
            rowData += '<td>🌐 web</td>';
        }


        rowData += `<td>${htmlEncode(passInfo.address)}</td>`;
        rowData += `<td>${htmlEncode(passInfo.username)}</td>`;
        rowData += `<td><span class='hidden' id='${parseInt(passInfo.id)}_visible'>${htmlEncode(passInfo.password)}</span><span id='${parseInt(passInfo.id)}_hidden'>********</span></td>`;
        rowData += `<td>${htmlEncode(passInfo.note)}</td>`;
        rowData += `<td>
                            <button type='button' class='btn btn-sm btn-dark btn-icon-text' onclick="togglePassView('${parseInt(passInfo.id)}')" id='${parseInt(passInfo.id)}_vBtn'>
                                <i class='mdi mdi-eye btn-icon'></i>
                            </button>
                            <button type='button' class='btn btn-sm btn-danger btn-icon-text'>
                                <i class='mdi mdi-delete btn-icon'></i>
                            </button>
                    </td>
            </tr>`;

        $('#password-listing > tbody:last-child').append(rowData);
    }

    $('#empty-table-msg').hide();
    $('#password-listing').show();

}

const toggleInputs = (state) => {
	$('#cancelBtn').prop('disabled', state);
	$('#addRecordBtn').prop('disabled', state);
}

const clearInputs = () => {
	$('#newRecordAddr').val('');
	$('#newRecordUser').val('');
	$('#newRecordPass').val('');
	$('#newRecordNote').val('');
}

const addRecord = async () => {

	toggleInputs(true);

	let card = $('#resp-msg');
	card.hide();


	let recType = $('#newRecordType').find(':selected').text();
	let recAddr = $('#newRecordAddr').val();
	let recUser = $('#newRecordUser').val();
	let recPass = $('#newRecordPass').val();
	let recNote = $('#newRecordNote').val();

	if ($.trim(recType) === '' || $.trim(recAddr) === '' || $.trim(recUser) === '' || $.trim(recPass) === '') {
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
                query: 'mutation($recType: String!, $recAddr: String!, $recUser: String!, $recPass: String!, $recNote: String!) { AddPhrase(recType: $recType, recAddr: $recAddr, recUser: $recUser, recPass: $recPass, recNote: $recNote) { message } }',
                variables: {
                    recType,
                    recAddr,
                    recUser,
                    recPass,
                    recNote
                }
            }),
		})
		.then((response) => response.json())
        .then((response) => {
            if (response.data.AddPhrase) {
                card.text(response.data.AddPhrase.message);
                card.attr('class', 'alert alert-success');
                card.show();
                loadPasswords();
                clearInputs();
                toggleInputs(false);
                window.setTimeout(function() {
                    $('#showFormBtn').click();
                    card.hide();
                }, 1000);
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

const htmlEncode = (str) => {
	return String(str).replace(/[^\w. ]/gi, function(c) {
		return '&#' + c.charCodeAt(0) + ';';
	});
}