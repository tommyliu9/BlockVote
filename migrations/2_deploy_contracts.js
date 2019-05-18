const HelloWorld = artifacts.require("HelloWorld");

module.exports = function(deployer) {
	deployer.deploy(HelloWorld, "hello");
	// additional contracts added here later
};
