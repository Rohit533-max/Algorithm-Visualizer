import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
arr = [40,30,20,10]
clock = pygame.time.Clock()

def bubble_sort(screen,nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            #show the comparison
            draw_array(screen,nums,(j,j+1))
            pygame.display.update()

            #to see the comparison
            pygame.time.delay(300)

            if nums[j] > nums[j+1]:  
                nums[j],nums[j+1] = nums[j+1],nums[j] 

            #show the swap
            draw_array(screen,nums,(j,j+1))
            pygame.display.update()

            #show the sorted array
            pygame.time.delay(300)


def draw_array(screen,nums,comparing = None):
    width,height = screen.get_size()
    bar_widht = width/len(nums)
    max_val = max(nums)

    for i,val in enumerate(nums):
        # to keep the bar height touch the top of window by 50
        bar_height = (val/max_val) * (height - 50)

        x = i * bar_widht
        y = height - bar_height

        if comparing and i in comparing:
            color = 'red'
        else:
            color = 'white'
        pygame.draw.rect(
            screen,
            color,
            (x,y,bar_widht,bar_height)
        )

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    bubble_sort(screen,arr)

    #showing the sorted array
    draw_array(screen,arr)
    pygame.display.update()

    pygame.time.delay(500)

pygame.quit()