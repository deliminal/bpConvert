import json
import sys
import base64
import gzip
import zlib
from pprint import pprint

class FactorioBlueprint:

  """Factorio Blueprint String Operations"""
  def __init__(self, blueprintString):
    self.raw = blueprintString
    

  # Getters
  @property
  def raw(self):
    return self._raw

  @property
  def version(self):
    return self.versionFromRaw()

  @property
  def asJson(self):
    return self.decodeJsonFromBluepringFormat()
  
  
  # Setters
  @raw.setter
  def raw(self,value):
    self._raw = value


  # Methods
  def __str__(self):
    return "%s" % (self.raw)

  def versionFromRaw(self):
    """Get the blueprint version from the raw string. This is typically the first byte."""
    if self.raw != None:
      return self.raw[:1]
    return None

  def decodeJsonFromBluepringFormat(self):
    """Decode the blueprint into JSON"""
    if self.raw != None:
      return json.loads(
      zlib.decompress(
        base64.b64decode(self.raw[1:])
        )
      )
    return None

  def encodeJsonToBlueprintFormat(editedJson, version=None):
    """Static function to encode json back to the Factorio blueprint format, using zlib and b64 encoding"""
    versionString = version if version != None else "0"
    return str(versionString + base64.b64encode(zlib.compress(json.dumps(editedJson).encode('utf8'))).decode('utf8'))

  def rebuildRaw(self, editedJson):
    """Rebuilds the _raw data from edited Json"""
    self.raw = FactorioBlueprint.encodeJsonToBlueprintFormat(editedJson,self.version)
    return self.raw

  def convertEntity(self,current,replacement):

    """Converts a single entity to another within the blueprint"""
    bpJson = self.asJson

    # icons
    for icon in bpJson["blueprint"]["icons"]:
      if icon["signal"]["name"] == current:
        icon["signal"]["name"] = replacement

    # entities
    for entity in bpJson["blueprint"]["entities"]:
      if entity["name"] == current:
        entity["name"] = replacement

    return self.rebuildRaw(bpJson)

