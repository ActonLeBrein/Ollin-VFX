import plugin_test

for i in plugin_test.getPlugins():
	print("Loading plugin " + i["name"])
	plugin = plugin_test.loadPlugin(i)
	plugin.run()