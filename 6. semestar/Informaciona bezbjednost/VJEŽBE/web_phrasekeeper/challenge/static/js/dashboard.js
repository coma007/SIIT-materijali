$("#showFormBtn").click(function() {
	if ($("#form-card").is(":hidden")) {
		$("#showFormBtn").find("i").attr("class", "mdi mdi-minus");
		$("#form-card").slideDown("slow");
	} else {
		$("#form-card").slideUp("slow");
		$("#showFormBtn").find("i").attr("class", "mdi mdi-plus");
	}
});


function togglePassView(pRowId) {
	$(`#${pRowId}_visible`).toggle();
	$(`#${pRowId}_hidden`).toggle();
	$(`#${pRowId}_vBtn`).find('i').first().toggleClass("mdi-eye mdi-eye-off");

}