var http = window.location.origin
$(document).ready(function () {


})
function homeList() {
    $.ajax({
        url: http + '/book',
        type: "GET",
        dataType: "json",
        success: (data) => {
            var html = '';
            $(data).each(function (index, value) {
                html += "<div class=" + 'article-metadata' + " ><h2><a class=" + 'article-title' + " href=" + http + '/book/detail/' + value.id + " >Title: " + value.title + "</a></h2>Author: "
                $(value.author_tags).each(function (index, value2) {
                    html += "<a class=" + 'mr-2' + "  >" + value2.author + " </a>"
                })
                html += "</div>"
            })

            $("#div1").append(html)

        },
        error: (error) => {

            $('#err').show()
            $("#err").html("Server error please refresh and try again")

        }
    });
};
function logout() {
    $.ajax({
        url: http + "/login-logout-user/",
        type: 'GET',
        sucess: (data) => {
            $('#message').show()
            $('#message').html('Successfully logged out')
            return true
        },
        error: (error) => {
            console.log(error)
        }
    })
};

function formatString(str) {
    return str
        .replace(/(\B)[^ ]*/g, match => (match.toLowerCase()))
        .replace(/^[^ ]/g, match => (match.toUpperCase()));
}

