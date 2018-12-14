const HellowTest = artifacts.require("./HelloWorld.sol")

contract('FishToken', async (accounts) => {
  const owner = accounts[0]

  let instance
  beforeEach('setup contract for each test', async () => {
    instance = await HellowTest.new()
  })

  it('test show', async () => {
    const currentShark = await instance.show()
  })
})