#include <iostream>
#include "OpenVolumeMesh/Geometry/VectorT.hh"
#include "OpenVolumeMesh/Mesh/PolyhedralMesh.hh"

using std::cout;
using std::endl;

using meshtp = OpenVolumeMesh::GeometricPolyhedralMeshV3f;
using OpenVolumeMesh::Geometry::Vec3f;

int main(int argc, char** argv)
{
  meshtp mesh;

  auto v0 = mesh.add_vertex(Vec3f(0.0,0.0,0.0));
  
  cout << "mesh object created" << endl;

}
