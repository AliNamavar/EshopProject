function send_Article_massage(articleId) {
    var comment = $('#commentText').val();
    var parent_id = $('#parent_id').val()

    $.get('/articles/comments', {
        article_comments: comment,
        article_id: articleId,
        parent_id: parent_id,

    }).then(res => {
        console.log(res);
        // location.reload();
        $('#comment_area').html(res);
        $('#commentText').val('');
        $('#parent_id').val('');
        if (parent_id !== null && parent_id !== '') {
            document.getElementById("single_comment_box_" + parent_id).scrollIntoView({behavior: 'smooth'});

        } else {
            document.getElementById("comment_area" + parent_id).scrollIntoView({behavior: 'smooth'});

        }

    });
}

function fillpatternid(parentId) {
    $('#parent_id').val(parentId)
    document.getElementById("commentForm").scrollIntoView({behavior: 'smooth'});

}

// function filterProduct(){
//     // debugger;
//     const filterPrice = $('#sl2').val();
//     const startPrice = filterPrice.split(',')[0];
//     const endPrice = filterPrice.split(',')[1];
//     $('start_price').val(startPrice);
//     $('end_price').val(endPrice);
// }

function filterProduct() {
    const filterPrice = $('#sl2').val();
    const startPrice = filterPrice.split(',')[0];
    const endPrice = filterPrice.split(',')[1];
    console.log('Filter Price:', filterPrice);

    $('#start_price').val(startPrice);
    $('#end_price').val(endPrice);


    $('#filter_form').submit();
}

function fillpage(page) {
    $('#page').val(page);
    $('#filter_form').submit();

}


// function addProductToCart(productId){
//     console.log(productId)
//     var count = $('#countProductOrder').val()
//     $.post('add-product-to-order', {'product_id': productId, 'count': count}).then(res =>{
//         console.log(res)
//     })  

// }

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


function addProductToCart(productId) {
    var count = $('#countProductOrder').val();
    $.ajax({
        type: 'POST',
        url: '/add-product-to-order',
        data: {
            'product_id': productId,
            'count': count
        },
        headers: {
            'X-CSRFToken': csrftoken
        },

        success: function (res) {
            Swal.fire({
                icon: res.icon,
                text: res.message
            }).then(confirm => {
                if (confirm.isConfirmed && res.status === 'not_auth') {
                    window.location.href = '/login'
                }
            })
        }
    });
}


function removeProductAsOrder(event, productId) {
    event.preventDefault();
    console.log(productId);
    $.ajax({
        type: 'GET',
        url: 'Order-delete-product',
        data: {
            'product_id': productId
        },
        success: function (res) {
            if (res.status === 'success') {
                $('#allOrderAjaxs').html(res.data)
            }
        }
    })
}

function editordercount(ProductId, status, event) {
    event.preventDefault()

    $.ajax({
        type: 'POST',
        url: 'order-edit-count',
        data: {
            'product_id': ProductId,
            'newCount': status,
            'csrfmiddlewaretoken': csrftoken
        },
        success: function (res) {
            if (res.status === 'success') {
                $('#allOrderAjaxs').html(res.data)
            }

        }
    })
}

$(document).ready(function() {
    $("#check-address-form").submit(function(event) {
        event.preventDefault();

        let address = $("#check-addres-input").val();
        console.log('address', address)

        $.ajax({
            url: "/check-address",
            type: "POST",
            data: { address: address },
            headers: {
                "X-CSRFToken": getCSRFToken()
            },
            success: function(res) {
                if (res.status === 'success'){
                swal.fire({
                    text :res.text,
                    icon :res.icon,
                    confirmButtonText : res.button

                });
            }},
            error: function(xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });
});

function getCSRFToken() {
    let cookies = document.cookie.split('; ');
    for (let cookie of cookies) {
        let [name, value] = cookie.split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return '';
}
