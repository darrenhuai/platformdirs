from __future__ import annotations

from typing import TYPE_CHECKING, cast

import pytest

if TYPE_CHECKING:
    from pathlib import Path

    from _pytest.fixtures import SubRequest

PROPS = (
    "user_data_dir",
    "user_config_dir",
    "user_cache_dir",
    "user_state_dir",
    "user_log_dir",
    "user_documents_dir",
    "user_downloads_dir",
    "user_pictures_dir",
    "user_videos_dir",
    "user_music_dir",
    "user_desktop_dir",
    "user_projects_dir",
    "user_publicshare_dir",
    "user_templates_dir",
    "user_fonts_dir",
    "user_preference_dir",
    "user_bin_dir",
    "site_bin_dir",
    "user_applications_dir",
    "user_runtime_dir",
    "site_data_dir",
    "site_config_dir",
    "site_cache_dir",
    "site_state_dir",
    "site_log_dir",
    "site_applications_dir",
    "site_runtime_dir",
)


@pytest.fixture(params=PROPS)
def func(request: SubRequest) -> str:
    return cast("str", request.param)


@pytest.fixture(params=PROPS)
def func_path(request: SubRequest) -> str:
    prop = cast("str", request.param)
    return prop.replace("_dir", "_path")


@pytest.fixture
def props() -> tuple[str, ...]:
    return PROPS


@pytest.fixture
def posix_tmp_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> str:
    # Unix paths in Windows tests need the temporary directory's drive as the current drive. Dropping the drive also
    # keeps the value absolute under posixpath, which is what the XDG variables are checked against.
    monkeypatch.chdir(tmp_path)
    return tmp_path.as_posix().removeprefix(tmp_path.drive)
