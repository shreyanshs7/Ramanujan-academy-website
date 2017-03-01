$(document).ready(function() {
//Function for preview image.
    $(function() {
        $(":file").change(function() {
            if (this.files && this.files[0]) {
                var reader = new FileReader();
                reader.onload = imageIsLoaded;
                reader.readAsDataURL(this.files[0]);
            }
        });
    });
    function imageIsLoaded(e) {
        $('#message').css("display", "none");
        $('#preview').css("display", "block");
        $('#previewimg').attr('src', e.target.result);
    };


//Function for deleting preview image.
    $("#deleteimg").click(function() {
        $('#preview').css("display", "none");
        $('#file').val("");
    });

//Function for displaying details of uploaded image.
    $("#submit").click(function() {
        $('#preview').css("display", "none");
        $('#message').css("display", "block");
    });
});
