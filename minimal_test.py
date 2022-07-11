"""A minimal bot test for bug finding and fixing"""
import discord.ext.test as dpytest
import pytest


@pytest.mark.asyncio
async def test_dummy_cog():
    """Test that a simple dummy command works"""
    await dpytest.message('?hello')
    # dpytest.verify_message("hello world")
    assert dpytest.get_message().content == "hello world"
