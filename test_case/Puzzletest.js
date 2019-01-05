const Puzzle = artifacts.require("./Puzzle.sol")
contract('Puzzle', async (accounts) => {
const owner = accounts[0]
let instance
beforeEach('setup contract for each test',async() => {
instance = await Puzzle.new()
})
it('test %d',async() => {
await instace.reward()
await instace.solution()
await instace.owner()
await instace.diff()
await instace.locked()
})
})
