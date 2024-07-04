class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        
        def depth_first_search(node):
            if node['id'] == target_id:
                return node
            for child in node.get('children', []):
                result = depth_first_search(child)
                if result is not None:
                    return result
            return None

        return depth_first_search(self.root)
