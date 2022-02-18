$(document).ready(function () {
    $('#errname').hide();
    $('#erremail').hide();
    $('#errmob').hide();
    $('#errpass1').hide();
    $('#errpass2').hide();

    var errname = true;
    var erremail = true;
    var errmob = true;
    var errpass1 = true;
    var errpass2 = true;

    $('#name').keyup(function () {
        username_check();
    });

    function username_check() {
        var u_name = $('#name').val();
        if (u_name.length == ""){
            $('#errname').show();
            $('#errname').html('. Please Fill The User Name');
            $('#errname').focus();
            errname = false;
            return false;
        }else if((u_name.length < 3) || (u_name.length > 20)){
            $('#errname').show();
            $('#errname').html('. User Name must greater than 2 and smaller than 20');
            $('#errname').focus();
            errname = false;
            return false;
        }
        else {
            $('#errname').hide();
        }
    }

    $('#mobno').keyup(function () {
        mobno_check();
    });
    function mobno_check() {
        var u_mobno = $('#mobno').val();
        if (u_mobno.length == ""){
            $('#errmob').show();
            $('#errmob').html('. Please Fill The User Mobno');
            $('#errmob').focus();
            errmob = false;
            return false;
        }else if((u_mobno.length != 10) || (isNaN(u_mobno))){
            $('#errmob').show();
            $('#errmob').html('. Mobile number must be 10 degits not Char');
            $('#errmob').focus();
            errmob = false;
            return false;
        }else {
            $('#errmob').hide();
        }
    }

    $('#email').keyup(function () {
        email_check();
    });
    function email_check() {
        var u_email = $('#email').val();
        var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
        if (u_email.length == ""){
            $('#erremail').show();
            $('#erremail').html('. Please Fill The User Email-id');
            $('#erremail').focus();
            erremail = false;
            return false;
        }else if(!u_email.match(pattern)){
            $('#erremail').show();
            $('#erremail').html('. Invalid User Email-id');
            $('#erremail').focus();
            erremail = false;
            return false;
        }else {
            $('#erremail').hide();
        }
    }

    $('#pass1').keyup(function () {
        pass1_check();
    });
    function pass1_check() {
        var u_pass1 = $('#pass1').val();
        var p_patern = /^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,15}$/;
        if (u_pass1.length == ""){
            $('#errpass1').show();
            $('#errpass1').html('. Please Fill The Password');
            $('#errpass1').focus();
            errpass1 = false;
            return false;
        }else if(!u_pass1.match(p_patern)){
            $('#errpass1').show();
            $('#errpass1').html('. password minimum six characters.<br>. password at least one lowercase letter.<br>. password contains one number.<br>. password contains one special character:');
            $('#errpass1').focus();
            errpass1 = false;
            return false;
        }else {
            $('#errpass1').hide();
        }
    }

    $('#pass2').keyup(function () {
        pass2_check();
    });
    function pass2_check() {
        var u_pass2 = $('#pass2').val();
        var u_pass1 = $('#pass1').val();
        if (u_pass2.length == ""){
            $('#errpass2').show();
            $('#errpass2').html('. Please Fill The Confirm Password');
            $('#errpass2').focus();
            errpass2 = false;
            return false;
        }else if(u_pass2 != u_pass1){
            $('#errpass2').show();
            $('#errpass2').html('. Password miss match');
            $('#errpass2').focus();
            errpass2 = false;
            return false;
        }else {
            $('#errpass2').hide();
        }
    }
    $("#btn-submit").click(function () {
        var errname = true;
        var erremail = true;
        var errmob = true;
        var errpass1 = true;
        var errpass2 = true;

        username_check();
        mobno_check();
        email_check();
        pass1_check();
        pass2_check();
        if ((errname==true) && (errmob==true) && (erremail==true) && (errpass1==true) && (errpass2==true) ){
            return true;
        }else {
            return false;
        }
    })
});