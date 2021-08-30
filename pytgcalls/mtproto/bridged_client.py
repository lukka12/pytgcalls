from typing import Any, Callable


class BridgedClient:

    async def get_call(
        self,
        chat_id: int,
    ):
        pass

    async def join_group_call(
        self,
        chat_id: int,
        json_join: dict,
        invite_hash: str,
        join_as: Any,
    ) -> dict:
        pass

    async def leave_group_call(
        self,
        chat_id: int,
    ):
        pass

    async def change_volume(
        self,
        chat_id: int,
        volume: int,
        participant: Any,
    ):
        pass

    async def resolve_peer(
        self,
        user_id: int,
    ):
        pass

    def is_connected(self) -> bool:
        pass

    async def start(self):
        pass

    @staticmethod
    def chat_id(input_peer):
        is_channel = hasattr(input_peer, 'channel_id')
        is_channel_update = input_peer.__class__.__name__ == 'Channel'
        is_chat = input_peer.__class__.__name__ == 'Chat'
        if is_channel:
            return -1000000000000 - input_peer.channel_id
        elif is_channel_update:
            return -1000000000000 - input_peer.id
        elif is_chat:
            return - input_peer.id
        else:
            return -input_peer.chat_id

    def on_closed_voice_chat(self) -> Callable:
        pass

    def on_kicked(self) -> Callable:
        pass

    def on_receive_invite(self) -> Callable:
        pass

    async def get_id(self) -> int:
        pass

    def on_left_group(self) -> Callable:
        pass

    async def get_full_chat(self, chat_id: int):
        pass