async def three_stages(request1):
    response1 = await api_call1(request1)
    # stage 1
    request2 = step1(response1)
    response2 = await api_call2(request2)
    # stage 2
    request3 = step2(response2)
    response3 = await api_call3(request3)
    # stage 3
    step3(response3)

# ...

loop.create_task(three_stages(request1))  # schedule execution
