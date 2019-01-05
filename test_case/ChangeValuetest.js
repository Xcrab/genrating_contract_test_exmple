const ChangeValue = artifacts.require("./ChangeValue.sol")
contract('ChangeValue', async (accounts) => {
const owner = accounts[0]
let instance
beforeEach('setup contract for each test',async() => {
instance = await ChangeValue.new()
})
it('test %d',async() => {
await instace.sub(85996507162976728050019613560223708094598514620668106886015967515166407617093)
await instace.add(3940580824104109485798150343350738243200082373079629205139461502943297142892,107581920609263001539212439589966285696900422098204975637003893915390072609)
await instace.tot()
})
})
