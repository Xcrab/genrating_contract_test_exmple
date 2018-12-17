const ChangeValue = artifacts.require("./ChangeValue.sol")
contract('ChangeValue', async (accounts) => {
const owner = accounts[0]
let instance
beforeEach('setup contract for each test',async() => {
instance = await ChangeValue.new()
})
it('test %d',async() => {
await instace.sub(102208152118028986502839184694344134840905319576143958974959116395000761535378)
await instace.add(114845968119172013451846447606210567865100916946330137149069643226359452592574,105117812901196473186428965381853340594157104943548653640249119915792388326351)
await instace.tot()
})
})
