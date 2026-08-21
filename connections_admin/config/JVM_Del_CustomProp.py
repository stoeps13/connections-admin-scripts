'''
IBM Connections Jython script

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

'''

# Jython script to remove JVM custom property 'org.eclipse.jst.j2ee.commonarchivecore.openAllArchives'
# from deployment manager, node agents, and all application servers

def removeJvmCustomProperty(serverName, nodeName, propertyName):
    """
    Remove a custom property from a server's JVM
    """
    try:
        # Get the server configuration
        server = AdminConfig.getid('/Cell:/Node:' + nodeName + '/Server:' + serverName + '/')
        if not server:
            print "Server " + serverName + " on node " + nodeName + " not found"
            return False
            
        # Get the JVM configuration
        jvm = AdminConfig.list('JavaVirtualMachine', server)
        if not jvm:
            print "JVM configuration not found for server " + serverName
            return False
            
        # Get all custom properties for the JVM
        customProps = AdminConfig.list('Property', jvm)
        
        # Look for the specific property
        propertyFound = False
        for prop in customProps.split('\n'):
            if prop.strip():
                propName = AdminConfig.showAttribute(prop, 'name')
                if propName == propertyName:
                    # Remove the property
                    AdminConfig.remove(prop)
                    print "Removed property '" + propertyName + "' from " + serverName + " on node " + nodeName
                    propertyFound = True
                    break
        
        if not propertyFound:
            print "Property '" + propertyName + "' not found on " + serverName + " on node " + nodeName
            
        return propertyFound
        
    except Exception, e:
        print "Error processing server " + serverName + " on node " + nodeName + ": " + str(e)
        return False

def main():
    """
    Main function to remove the custom property from all servers
    """
    propertyName = 'org.eclipse.jst.j2ee.commonarchivecore.openAllArchives'
    serversProcessed = 0
    propertiesRemoved = 0
    
    print "Starting removal of JVM custom property: " + propertyName
    print "=" * 60
    
    try:
        # Get all cells
        cells = AdminConfig.list('Cell').split('\n')
        
        for cell in cells:
            if not cell.strip():
                continue
                
            cellName = AdminConfig.showAttribute(cell, 'name')
            print "\nProcessing Cell: " + cellName
            
            # Get all nodes in the cell
            nodes = AdminConfig.list('Node', cell).split('\n')
            
            for node in nodes:
                if not node.strip():
                    continue
                    
                nodeName = AdminConfig.showAttribute(node, 'name')
                print "\n  Processing Node: " + nodeName
                
                # Get all servers in the node
                servers = AdminConfig.list('Server', node).split('\n')
                
                for server in servers:
                    if not server.strip():
                        continue
                        
                    serverName = AdminConfig.showAttribute(server, 'name')
                    serverType = AdminConfig.showAttribute(server, 'serverType')
                    
                    # Process deployment manager, node agents, and application servers
                    if serverType in ['DEPLOYMENT_MANAGER', 'NODE_AGENT', 'APPLICATION_SERVER']:
                        print "    Processing " + serverType + ": " + serverName
                        serversProcessed += 1
                        
                        if removeJvmCustomProperty(serverName, nodeName, propertyName):
                            propertiesRemoved += 1
        
        print "\n" + "=" * 60
        print "Summary:"
        print "  Servers processed: " + str(serversProcessed)
        print "  Properties removed: " + str(propertiesRemoved)
        
        if propertiesRemoved > 0:
            print "\nSaving configuration changes..."
            AdminConfig.save()
            print "Configuration saved successfully!"
            print "\nNOTE: You will need to restart the affected servers for the changes to take effect."
        else:
            print "\nNo properties were removed. No configuration changes to save."
            
    except Exception, e:
        print "Error in main execution: " + str(e)
        return False
    
    return True

# Execute the main function
if __name__ == '__main__' or __name__ == 'main':
    main()
