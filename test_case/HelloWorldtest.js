const HelloWorld = artifacts.require("./HelloWorld.sol")
contract('HelloWorld', async (accounts) => {
const owner = accounts[0]
let instance
beforeEach('setup contract for each test',async() => {
instance = await HelloWorld.new()
})
it('test %d',async() => {
await instace.add(-42930600106607958542627454627111081092050592595342269954009575941418204195240,-34549603586902414609326832087416739325244410709806131725704399996762271738262)
await instace.sub(19752367437312139980145084042678946524032008579787815066641916218838049716046,-44353152591288623916378060780341753134531454520880382512890048473019383133923)
await instace.show()
})
})