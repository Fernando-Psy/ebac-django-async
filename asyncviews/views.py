from django.http import JsonResponse
import asyncio
import httpx

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(f"Async call {num} completed")
        async with httpx.AsyncClient() as client:
            response = await client.get('https://httpbin.org/')
            print(f"Response {num}: {response.status_code}")
            print(f"Response content {num}: {response.text[:100]}")

async def api_view(request):
    await http_call_async()
    return JsonResponse({"message": "Async request completed."})