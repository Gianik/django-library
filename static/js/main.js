
$(document).ready(function () {
    var httpub = 'http://127.0.0.1:8000/book/'


})
function homeList() {
    $.ajax({
        url: 'http://127.0.0.1:8000/book',
        type: "GET",
        dataType: "json",
        success: (data) => {
            var html = '';
            $(data).each(function (index, value) {
                html += "<div class=" + 'article-metadata' + " ><h2><a class=" + 'article-title' + " href=" + 'http://127.0.0.1:8000/book/detail/' + value.id + " >Title: " + value.title + "</a></h2>Author: "
                $(value.author).each(function (index, value2) {
                    html += "<a class=" + 'mr-2' + "  >" + value2.full_name + " </a>"
                })
                html += "</div>"
            })

            $("#div1").append(html)

        },
        error: (error) => {
            console.log(error);
        }
    });
};
function logout() {
    $.ajax({
        url: "http://127.0.0.1:8000/login-logout-user/",
        type: 'GET',
        sucess: (data) => {
            // window.location.replace("http://127.0.0.1:8000/logout")
            return true
        },
        error: (error) => {
            console.log(error)
        }
    })
}