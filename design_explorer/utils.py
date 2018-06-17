import json
from design_explorer import graph


def add_nodes_to_dictionary(dTraceFile, dJsonFile):
    if 'node' in dJsonFile:
        for sNode in dJsonFile['node']:
            dTraceFile['node'][sNode] = dJsonFile['node'][sNode]


def add_edges_to_dictionary(dTraceFile, dJsonFile):
    if 'edge' in dJsonFile:
        for sEdge in dJsonFile['edge']:
            dTraceFile['edge'][sEdge] = dJsonFile['edge'][sEdge]


def add_traces_to_dictionary(dTraceFile, dJsonFile):
    if 'trace' in dJsonFile:
        for sTrace in dJsonFile['trace']:
            dTraceFile['trace'][sTrace] = dJsonFile['trace'][sTrace]


def create_empty_trace_dictionary():
    dTraceFile = {}
    dTraceFile['node'] = {}
    dTraceFile['edge'] = {}
    dTraceFile['trace'] = {}
    return dTraceFile


def read_trace_file(commandLineArguments):
    dTraceFile = create_empty_trace_dictionary()
    for sTraceFile in commandLineArguments.tracefile:
        with open(sTraceFile) as json_file:
            dJsonFile = json.load(json_file)

        add_nodes_to_dictionary(dTraceFile, dJsonFile)
        add_edges_to_dictionary(dTraceFile, dJsonFile)
        add_traces_to_dictionary(dTraceFile, dJsonFile)

    return dTraceFile


def build_node_list(dTracefile):
    oNodeList = graph.base_list()
    for sNode in dTracefile['node']:
        oNode = graph.node(sNode)
        if 'subNode' in dTracefile['node'][sNode]:
            oNode.subNode = dTracefile['node'][sNode]['subNode']
        oNodeList.add_item(oNode)
    return oNodeList


def build_edge_list(dTracefile):
    oEdgeList = graph.base_list()
    for sEdge in dTracefile['edge']:
        oEdge = graph.edge()
        oEdge.source = dTracefile['edge'][sEdge]['source']
        oEdge.target = dTracefile['edge'][sEdge]['target']
        oEdge.interface = dTracefile['edge'][sEdge]['interface']
        oEdge.name = sEdge
        oEdgeList.add_item(oEdge)
    return oEdgeList


def build_trace_list(dTracefile):
    oTraceList = graph.base_list()
    for sTrace in dTracefile['trace']:
        oTrace = graph.trace(sTrace)
        oTrace.path = dTracefile['trace'][sTrace]['path']
        oTraceList.add_item(oTrace)
    return oTraceList


def process_trace(lTrace, oTrace, oEdgeList, oTraceList):

    for sPath in oTrace.path:
        if oEdgeList.get_item(sPath):
            lTrace.add_to_path(oEdgeList.get_item(sPath))
        if oTraceList.get_item(sPath):
            process_trace(lTrace, oTraceList.get_item(sPath), oEdgeList, oTraceList)
