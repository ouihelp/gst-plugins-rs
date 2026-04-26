# gst-plugins-rs wheel

This Python wheel packages the `rswebrtc` GStreamer plugin for OuiHelp local development.

Typical usage:

1. `brew install gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad`
2. `uv sync`
3. In Python, detect the package and prepend `gst_plugins_rs.gst_plugin_dir()` to `GST_PLUGIN_PATH` / `GST_PLUGIN_PATH_1_0` before initializing GStreamer.

The wheel is built on tags and published to AWS CodeArtifact.
