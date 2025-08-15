import importlib
import pkgutil
from pathlib import Path
from tasklin.providers import AIProvider

PROVIDERS = {}


def load_providers(user_providers_path=None):
    # Scan built-in providers
    package = "tasklin.providers"
    for _, name, _ in pkgutil.iter_modules([str(Path(__file__).parent / "providers")]):
        module = importlib.import_module(f"{package}.{name}")
        register_provider_from_module(module)

    if user_providers_path is None:
        user_path = Path.cwd() / "providers"
    else:
        user_path = Path(user_providers_path)

    if user_path.exists():
        for file in user_path.glob("*.py"):
            if file.name != "__init__.py":
                module_name = file.stem
                spec = importlib.util.spec_from_file_location(module_name, file)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                register_provider_from_module(mod)


def register_provider_from_module(module):
    for attr_name in dir(module):
        obj = getattr(module, attr_name)
        if (
            isinstance(obj, type)
            and issubclass(obj, AIProvider)
            and obj is not AIProvider
        ):
            PROVIDERS[obj.name] = obj


def get_provider(provider_type, user_providers_path=None, **kwargs):
    if not PROVIDERS:
        load_providers(user_providers_path)
    provider_class = PROVIDERS.get(provider_type)
    if not provider_class:
        raise ValueError(f"Provider '{provider_type}' not found.")
    return provider_class(**kwargs)
