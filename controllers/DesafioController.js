const Desafio = require("../models/Desafio");
const db = require("../database/database");

class DesafioController {
    async getDesafios() {
        const desafios = await Desafio.findAll()
            .then(desafios => {
                const res = { data: [], email: "thicesar25@gmail.com" };
                res.data = desafios.map(desafio => {
                    let { date, teams, away, home } = desafio.dataValues;
                    date.setHours(date.getHours() + 3);
                    const dia = date.getDate().toString().padStart(2, "0");
                    const mes = (date.getMonth() + 1).toString().padStart(2, "0");
                    const ano = date.getFullYear();
                    const hora = date.getHours().toString().padStart(2, "0");
                    const minuto = date.getMinutes().toString().padStart(2, "0");
                    date = (dia + "/" + mes + "/" + ano + " " + hora + ":" + minuto);
                    home = parseFloat(home).toFixed(2);
                    away = parseFloat(away).toFixed(2);
                    const novoDesafio = { date, teams, away, home };
                    return (novoDesafio)
                })
                return res;
            });
        return desafios
    }
}

module.exports = new DesafioController();