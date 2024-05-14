const body = document.body; 
document.querySelectorAll("button").forEach((button) => {
    if(button.id != "automatic"){
        button.addEventListener("click", (e) => {
            body.style.backgroundColor = e.target.id;
        })
    }else{
        button.addEventListener("click", (e) => {
            body.style.backgroundColor = "white"
            setInterval(() => {
                if(body.style.backgroundColor == "white"){
                    body.style.backgroundColor = "red"
                }else if(body.style.backgroundColor == "red"){
                    body.style.backgroundColor = "green"
                }else if (body.style.backgroundColor == "green"){
                    body.style.backgroundColor = "yellow"
                }else if (body.style.backgroundColor == "yellow"){
                    body.style.backgroundColor = "white"
                }
            }, 2000)
        })
    }
})