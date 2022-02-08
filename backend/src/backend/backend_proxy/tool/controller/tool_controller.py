import datetime
from backend.backend_proxy.db.mongoDB import MongoDB
from backend.backend_proxy.tool.controller.abstract_controller import AbstractToolController
from backend.backend_proxy.tool.schema import ToolSchema
from backend.backend_proxy.tool.tool_class import Tool

from bson.objectid import ObjectId


class ToolController(AbstractToolController):
    __instance__ = None
    schema:ToolSchema =  ToolSchema()

    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = object.__new__(cls)
        return cls.__instance__

    def __init__(self) -> None:
        self.collection = MongoDB.get_collection("tool")

    def get_tool(self, tool_id: str) -> Tool:
        tool_dict = self.collection.find_one({"_id": ObjectId(tool_id)})
        if tool_dict is None:
            return None
        return self.schema.create_object(tool_dict)

    def get_tool_query(self, query: dict) -> Tool:
        tool_dict = self.collection.find_one(query)
        if tool_dict is None:
            return None
        return self.schema.create_object(tool_dict)

    def create_tool(self, tool_info: dict) -> Tool:
        tool_info['registered_at'] = datetime.datetime.now().strftime(
            '%Y-%m-%dT%H:%M:%S')

        created_tool: Tool = self.schema.create_object(tool_info)
        inserted_object = self.collection.insert_one(
            self.schema.dump(created_tool))
        return self.get_tool(tool_id=inserted_object.inserted_id)

    def update_tool(self, tool_id: str, tool_info: dict) -> Tool:
        del tool_info['_id']
        self.collection.update_one(
            {"_id": ObjectId(tool_id)}, {"$set": tool_info})

    def get_all_tools(self) -> list[Tool]:
        return [self.schema.create_object(x) for x in self.collection.find({})]

    def dump_tool(self, tool:Tool) -> dict: return self.schema.dump(tool=tool)
