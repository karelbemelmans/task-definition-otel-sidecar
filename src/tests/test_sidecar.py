import unittest
from sidecar import SidecarGenerator


class TestSidecar(unittest.TestCase):

    # Example data of a task definition
    taskDefinition = {
        "containerDefinitions": [
            {
                "name": "my-container",
                "image": "my-image"
            }
        ]
    }

    def test_sidear_with_valid_input(self):

        name = "otel"
        image = "otel/opentelemetry-collector-contrib"

        expectedTaskDefinition = {
            "containerDefinitions": [
                {
                    "name": "my-container",
                    "image": "my-image"
                },
                {
                    "name": "otel",
                    "image": "otel/opentelemetry-collector-contrib"
                }
            ]
        }

        s = SidecarGenerator(name=name, image=image)
        generated = s.addOtelSidecar(self.taskDefinition)
        self.assertEqual(generated, expectedTaskDefinition)


if __name__ == '__main__':
    unittest.main()
