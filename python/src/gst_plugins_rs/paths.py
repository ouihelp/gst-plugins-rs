from importlib.resources import files


def gst_plugin_dir() -> str:
    return str(files("gst_plugins_rs").joinpath("lib", "gstreamer-1.0"))
