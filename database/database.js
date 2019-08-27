const Sequelize = require("sequelize");
const fs = require("fs");

const dbConfig = JSON.parse(fs.readFileSync(__dirname + "/settings.json", "utf-8"));

const db = new Sequelize(dbConfig.database, dbConfig.user, dbConfig.password, {
    host: dbConfig.host,
    dialect: dbConfig.dialect
});

module.exports = db;