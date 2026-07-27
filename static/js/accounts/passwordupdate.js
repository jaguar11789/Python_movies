function passwordUpdate() {
    const currentPassword = document.getElementById('current_password').value;
    const password        = document.getElementById('password').value;
    const passwordCheck   = document.getElementById('userPwdCheck').value;

    if (password.length < 9 || password.length > 18) {
            alert('비밀번호는 9자리 이상 18자리 이하로 입력하세요.');

            return;
    }
    if (password !== passwordCheck) {
        //document.getElementById('passwordError').textContent = '새 비밀번호가 일치하지 않습니다.';
        alert('새 비밀번호가 일치하지 않습니다.');

        return;
    }
    if (!confirm('입력하신 비밀번호로 수정 하시겠습니까?')) {

        return;
    }
    fetch(passwordUpdateUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            current_password: currentPassword,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            location.href = loginUrl;
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error(error);
    });
}