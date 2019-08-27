const Sequelize = require("sequelize");
const db = require("../database/database");

const Jogo = db.define(
    "desafio",
    {
        teams: {
            type: Sequelize.STRING(36)
        },
        away: {
            type: Sequelize.STRING(36)
        },
        home: {
            type: Sequelize.STRING(36)
        },
        date: {
            type: Sequelize.DATE,
            get: function() {
                return moment(this.getDataValue("date")).format("DD/MM/YYYY HH:mm");
            }
        }
    },
    {
        timestamps: false,
        freezeTableName: true,
        tableName: "desafio"
    }
);

module.exports = Jogo;