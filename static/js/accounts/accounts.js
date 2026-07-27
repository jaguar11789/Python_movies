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

$('#userId').on('blur', function () {

    const idPattern = /^[a-zA-Z0-9_-]{8,15}$/;

    const username = $(this).val().trim();

    if (username === '') {
        // 아무것도 입력하지 않은 경우
        return;

    } else if ((username.length < 8 || username.length > 15) || !idPattern.test(username)) {
        alert('아이디는 8~15자의 영문, 숫자, -, _만 사용할 수 있습니다.');

        $(this).val('');
        $('#id_ok').hide();
        $('#id_already').hide();
    } else {
        // 아이디가 8~15자인 경우
        // 여기서 AJAX 중복 확인
        $.ajax({
            url: '/accounts/check-username/',
            type: 'GET',
            data: {
                username: username
            },

            success: function (data) {

                if (data.exists) {
                    $('#id_ok').hide();
                    $('#id_already').show();

                } else {
                    $('#id_ok').show();
                    $('#id_already').hide();
                }
            },

            error: function () {
                console.log('아이디 중복 확인 요청 실패');
            }
        });
    }
});

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

const currentPassword = document.querySelector('#current_password');
const passwordError = document.querySelector('#passwordError');

if (currentPassword && passwordError) {
    currentPassword.addEventListener('input', function () {
        passwordError.style.display = 'none';
    });
}

function accountDelete() {
    const withdrawReason = document.getElementById('withdrawReason').value;

    if (withdrawReason === '') {
        alert('탈퇴 사유를 선택해주세요.');

        return;
    }
    if (!confirm('정말 회원 탈퇴를 하시겠습니까?')) {

        return;
    }
    fetch(accountDeleteUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            reason: withdrawReason
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            location.href = mainUrl;
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error(error);
        alert('회원 탈퇴 중 오류가 발생했습니다.')
        location.href = mainUrl;
    });
}