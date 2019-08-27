const DesafioController = require("./controllers/DesafioController");
const axios = require("axios");

(async function() {
    const desafios = await DesafioController.getDesafios();
    axios.post("http://desafio.logus.tech/desafio", desafios)
        .then(res => { console.log(res)})
        .catch(err => { console.log(err.response.data)});
})();