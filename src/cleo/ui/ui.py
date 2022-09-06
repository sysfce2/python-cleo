from __future__ import annotations

from cleo.exceptions import ValueException
from cleo.ui.component import Component


class UI:
    def __init__(self, components: list[Component] | None = None) -> None:
        self._components: dict[str, Component] = {}

        if components is None:
            components = []

        for component in components:
            self.register(component)

    def register(self, component: Component) -> None:
        if not isinstance(component, Component):
            raise ValueException(
                "A UI component must inherit from the Component class."
            )

        if not component.name:
            raise ValueException("A UI component cannot be anonymous.")

        self._components[component.name] = component

    def component(self, name: str) -> Component:
        if name not in self._components:
            raise ValueException(f'UI component "{name}" does not exist.')

        return self._components[name]