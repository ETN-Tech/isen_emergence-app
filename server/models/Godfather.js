/**
 * GODFATHER MODEL
 * Create a Godfather model with its attributes
 * Create association with Account model
 */

const Account = require("./Account");
const { sequelize, Model, DataTypes } = require("../utils/database");

class Godfather extends Model {}

Godfather.init({
    fkAccountId: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        allowNull: false,
        references : {
            model: 'Accounts',
            key: 'accountId'
        }
    },
    phone: {
        type: DataTypes.STRING
    },
    isArchived: {
        type: DataTypes.BOOLEAN,
        defaultValue: false,
        allowNull: false
    }
}, {
    sequelize,
    modelName: 'Godfather'
})

// Create association with Account, a Godfather extends an Account
Godfather.Account = Godfather.belongsTo(Account, {
    foreignKey: 'fkAccountId'
})

module.exports = Godfather
