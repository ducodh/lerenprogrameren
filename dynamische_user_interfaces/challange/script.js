let naamingelogd = "";

function handleLogin(){
    let naam = document.getElementById("inputNaam").value;
    console.log("u hebt op de button geklikt");
    if (naamingelogd === ""){
        naamingelogd= naam;
        console.log("u bent ingelogd: " + naam);
        document.getElementById("inputNaam").value = "";
    }
}

