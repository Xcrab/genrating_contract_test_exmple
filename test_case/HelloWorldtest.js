const HelloWorld = artifacts.require("./HelloWorld.sol")
contract('HelloWorld', async (accounts) => {
const owner = accounts[0]
let instance
beforeEach('setup contract for each test',async() => {
instance = await HelloWorld.new()
})
it('test %d',async() => {
await instace.add(-33221121132573406663882220226591589707767543417948971728512212971798892193841,16934920690495726668223511721554796051745777407715340905429165864724397416593)
await instace.sub(1038981166631017591877086491570478910026000072311911483533060551557678633130,18389563619821868040594908432816909489385938713770320353889375375624643372315)
await instace.show()
})
})
