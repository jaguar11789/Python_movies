function addr_search() {
    new daum.Postcode({
        oncomplete: function (data) {

            console.log(data);

            var roadAddr  = data.roadAddress;  //도로명 주소 변수
            var jibunAddr = data.jibunAddress; //지번 주소 변수

            document.getElementById('zipcode').value = data.zonecode;

            if (roadAddr !== '') {
                document.getElementById('base_addr').value = roadAddr;
            } else if (jibunAddr !== '') {
                document.getElementById('base_addr').value = jibunAddr;
            }
        }
    }).open();
}

$(function () {

    $('#userPwdCheck').blur(function () {

        const password = $('#password').val();
        const passwordCheck = $('#userPwdCheck').val();

        // 비밀번호 길이 확인
        if (password.length < 9 || password.length > 18) {
            alert('비밀번호는 9자리 이상 18자리 이하로 입력하세요.');

            $('#password').val('');
            $('#userPwdCheck').val('');

            $('.pwd_ok').hide();
            $('.pwd_no').hide();

            return;
        }

        // 비밀번호 확인
        if (password === passwordCheck) {
            $('.pwd_ok').show();
            $('.pwd_no').hide();
        } else {
            $('#userPwdCheck').val('');
            $('.pwd_ok').hide();
            $('.pwd_no').show();

            // focus() 하지 않는다.
        }
    });
});