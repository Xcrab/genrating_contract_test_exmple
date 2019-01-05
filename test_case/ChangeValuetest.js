const ChangeValue = artifacts.require("./ChangeValue.sol")
contract('ChangeValue', async (accounts) => {
const owner = accounts[0]
let instance
beforeEach('setup contract for each test',async() => {
instance = await ChangeValue.new()
})
it('test %d',async() => {
await instace.sub(98397063696699453452933512135454978787522201175826175297707572929130428595335)
await instace.add(76595686008591164687371001832161671865960758767256121841722042408043221258608,80113068029368892174212138791210790987589015987254651099250393568421470692350)
await instace.tot()
})
})
